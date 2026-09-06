from pathlib import Path
import json
import re
import sys

INDEX_PATH = Path("index.html")
QUEUE_PATH = Path("tracker-sync-queue.json")

STATUS_RANK = {
    "active": 1,
    "cv_requested": 2,
    "followup": 2,
    "submitted": 3,
    "interview": 4,
    "rejected_employer": 5,
    "withdrawn": 5,
    "inactive": 5,
}


def normalize_url(url):
    return (url or "").strip().rstrip("/").lower()


def remove_detail(text, jid):
    pattern = re.compile(r'^\s*"' + re.escape(jid) + r'"\s*:\s*\{.*\},?\s*$', re.M)
    return pattern.subn('', text, count=1)


def main():
    source = INDEX_PATH.read_text(encoding="utf-8")
    original = source
    queue = json.loads(QUEUE_PATH.read_text(encoding="utf-8"))

    jobs_start = '    const jobs = [\n'
    jobs_end = '\n    ];\n\n    const detailById='
    if jobs_start not in source or jobs_end not in source:
        raise RuntimeError("Could not locate jobs data block")

    pre, remainder = source.split(jobs_start, 1)
    jobs_body, post = remainder.split(jobs_end, 1)

    jobs = []
    indent_by_id = {}
    for line in jobs_body.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        raw = stripped[:-1] if stripped.endswith(',') else stripped
        try:
            rec = json.loads(raw)
        except Exception as exc:
            raise RuntimeError(f"Invalid job record: {stripped[:120]}") from exc
        jobs.append(rec)
        indent_by_id[rec["id"]] = line[: len(line) - len(line.lstrip())]

    by_id = {j["id"]: j for j in jobs}

    for incoming in queue.get("jobUpserts", []):
        if "id" not in incoming:
            raise RuntimeError("jobUpsert is missing id")
        jid = incoming["id"]
        if jid in by_id:
            current = by_id[jid]
            patch = dict(incoming)
            if "status" in patch:
                old_status = current.get("status")
                new_status = patch.get("status")
                cv_ready_transition = (
                    old_status == "cv_requested"
                    and new_status == "active"
                    and bool(patch.get("cv") or current.get("cv"))
                )
                if STATUS_RANK.get(old_status, 0) > STATUS_RANK.get(new_status, 0) and not cv_ready_transition:
                    patch.pop("status")
            current.update(patch)
        else:
            incoming_url = normalize_url(incoming.get("job"))
            if incoming_url:
                dupe = next((j for j in jobs if normalize_url(j.get("job")) == incoming_url), None)
                if dupe:
                    raise RuntimeError(f"Duplicate URL for new job {jid}; existing id={dupe['id']}")
            jobs.insert(0, dict(incoming))
            by_id[jid] = jobs[0]
            indent_by_id[jid] = "      "

    remove_ids = set(queue.get("removeJobIds", []))
    jobs = [j for j in jobs if j.get("id") not in remove_ids]

    seen_urls = {}
    for j in jobs:
        url = normalize_url(j.get("job"))
        if not url:
            continue
        if url in seen_urls:
            raise RuntimeError(f"Duplicate job URL remains: {j['id']} and {seen_urls[url]}")
        seen_urls[url] = j["id"]

    rebuilt_jobs = []
    for i, rec in enumerate(jobs):
        indent = indent_by_id.get(rec["id"], "      ")
        encoded = json.dumps(rec, ensure_ascii=False, separators=(",", ":"))
        rebuilt_jobs.append(indent + encoded + ("," if i < len(jobs) - 1 else ""))

    source = pre + jobs_start + "\n".join(rebuilt_jobs) + jobs_end + post

    for jid in queue.get("removeDetailIds", []):
        source, _ = remove_detail(source, jid)

    detail_marker = '    const detailById={\n'
    if detail_marker not in source:
        raise RuntimeError("Could not locate detailById block")

    for item in queue.get("detailUpserts", []):
        jid = item.get("id")
        detail = item.get("detail")
        if not jid or not isinstance(detail, dict):
            raise RuntimeError("detailUpsert requires id and detail object")
        source, _ = remove_detail(source, jid)
        detail_line = (
            '      '
            + json.dumps(jid, ensure_ascii=False)
            + ':'
            + json.dumps(detail, ensure_ascii=False, separators=(",", ":"))
            + ',\n'
        )
        source = source.replace(detail_marker, detail_marker + detail_line, 1)

    if queue.get("upgradeSyncButton"):
        old_button = '<button id="copySummary">העתק סיכום לסנכרון</button>'
        new_button = '<button id="copySummary">העתק שינויים לסנכרון</button>'
        if source.count(old_button) == 1:
            source = source.replace(old_button, new_button, 1)
        elif source.count(new_button) != 1:
            raise RuntimeError("Sync button label is in an unexpected state")

        old_footer = 'כדי לעדכן גם את קובצי המעקב הקבועים, יש להעתיק את הסיכום ולהדביק בשיחה.'
        new_footer = 'כדי לסנכרן שינויי סטטוס מקומיים ל-GitHub, יש להעתיק את השינויים ולהדביק בשיחה; לאחר אישור הסנכרון ניתן לסמן אותם כסונכרנו.'
        if old_footer in source:
            source = source.replace(old_footer, new_footer, 1)

        start = '    document.getElementById("copySummary").addEventListener("click",async function(){\n'
        end = '    document.getElementById("copyCvQueue").addEventListener'
        if start not in source or end not in source:
            raise RuntimeError("Could not locate copySummary handler")
        head, tail = source.split(start, 1)
        _, rest = tail.split(end, 1)
        new_handler = (
            '    document.getElementById("copySummary").addEventListener("click",async function(){\n'
            '      const payload={type:"job_tracker_sync_delta",version:1,generatedAt:new Date().toISOString(),changes:changes.map(function(x){return{id:x.id,company:x.company,role:x.role,from:x.from,to:x.to,updated:x.updated,reason:x.reason||"",note:x.note||"",next:x.next||"",nextDate:x.nextDate||""};})};\n'
            '      if(!payload.changes.length){alert("אין שינויים מקומיים חדשים לסנכרון.");return;}\n'
            '      const text=JSON.stringify(payload,null,2);try{await navigator.clipboard.writeText(text);alert(payload.changes.length+" שינויים הועתקו לסנכרון. הדבק אותם בשיחת ChatGPT; אחרי שהסנכרון ל-GitHub הושלם, לחץ על \'סמן שינויים כסונכרנו\'.");}catch(e){window.prompt("העתק את השינויים לסנכרון:",text);}\n'
            '    });\n'
        )
        source = head + new_handler + end + rest

    if source == original:
        print("No changes required")
        return

    if source.count('const jobs = [') != 1 or source.count('const detailById=') != 1:
        raise RuntimeError("Tracker structure validation failed")
    if 'document.getElementById("copyCvQueue")' not in source or 'function render()' not in source:
        raise RuntimeError("Core tracker JS validation failed")

    INDEX_PATH.write_text(source, encoding="utf-8")
    print(f"Applied queue {queue.get('requestId', 'unknown')}; jobs={len(jobs)}")


if __name__ == "__main__":
    main()
