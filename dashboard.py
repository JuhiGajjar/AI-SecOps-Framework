import os
import sqlite3

# Cross-platform pathing for the root directory execution
DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "data", "database.db"))

def run():
    if not os.path.exists(DB_PATH):
        print("❌ Error: Database not found. Run 'python -m scanner.generator' first.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT scan_id, timestamp, total_tests, failed_tests, avg_risk_score, status FROM scans ORDER BY scan_id DESC LIMIT 1")
    latest = cursor.fetchone()
    
    if not latest:
        print("⚠️ No scans found.")
        return

    print("\n" + "="*70)
    print(" 🛡️  AI-SECOPS ASSESSMENT FRAMEWORK - LOG TERMINAL")
    print("="*70)
    print(f" LATEST RUN: #{latest[0]} | TIMESTAMP: {latest[1]}")
    print(f" AUDIT RESULT: {latest[5]}")
    print(f" STATUS: {latest[3]} Flaws Found out of {latest[2]} Injection Attempts")
    print(f" AVERAGE FRAMEWORK RISK INDEX: {latest[4]} / 10.0")
    print("="*70)

    cursor.execute("SELECT category, severity, payload, output, status, risk_score, recommendation FROM scan_results WHERE scan_id = ?", (latest[0],))
    results = cursor.fetchall()

    print("\n 🔍 DETAILED THREAT VECTOR BREAKDOWN:")
    print("-" * 70)
    for idx, row in enumerate(results, 1):
        print(f" [{idx}] VULNERABILITY STATUS: [{row[4]}]")
        print(f"     • Threat Class:    {row[0]} (Severity: {row[1]})")
        print(f"     • Calculated Risk: {row[5]} / 10.0")
        print(f"     • Attack Payload:  \"{row[2]}\"")
        print(f"     • Target Output:   \"{row[3]}\"")
        print(f"     • Fix Guidance:    {row[6]}")
        print("-" * 70)
        
    conn.close()

if __name__ == "__main__":
    run()
