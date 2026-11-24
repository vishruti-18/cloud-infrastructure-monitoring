
from pathlib import Path
from datetime import datetime

# Define file locations
log_file = Path("logs/system-health.log")
report_dir = Path("reports")
report_file = report_dir / "log-analysis-report.txt"

# Check whether log file exists
if not log_file.exists():
    print("Log file not found!")
    raise SystemExit(1)

# Create reports directory
report_dir.mkdir(parents=True, exist_ok=True)

# Read log entries
with log_file.open("r") as file:
    logs = file.readlines()

# Initialize counters
info_count = 0
warning_count = 0
error_count = 0

# Store warning and error messages
issues = []

# Analyze logs
for line in logs:

    if " - INFO - " in line:
        info_count += 1

    elif " - WARNING - " in line:
        warning_count += 1
        issues.append(line.strip())

    elif " - ERROR - " in line:
        error_count += 1
        issues.append(line.strip())

# Determine overall status
if error_count > 0:
    overall_status = "ERROR"
elif warning_count > 0:
    overall_status = "WARNING"
else:
    overall_status = "HEALTHY"

# Build report
report = f"""
========================================
       LOG ANALYSIS REPORT
========================================

Generated At: {datetime.now()}

Total Log Entries: {len(logs)}

INFO Count: {info_count}
WARNING Count: {warning_count}
ERROR Count: {error_count}

Overall Status: {overall_status}

Issues Detected:
"""

if issues:
    report += "\n" + "\n".join(issues)
else:
    report += "\nNo issues detected."

report += "\n\n========================================\n"

# Display report
print(report)

# Save report
report_file.write_text(report, encoding="utf-8")

print(f"Report saved at: {report_file}")
