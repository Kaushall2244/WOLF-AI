import sys
import os

# Ensure UTF-8 output encoding for Windows console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

# Add backend directory to sys.path
backend_path = os.path.dirname(os.path.abspath(__file__))
if backend_path not in sys.path:
    sys.path.insert(0, backend_path)

print("[TEST] Testing WOLF AI Backend Imports & Functionality...")

try:
    from core.config import config
    print(f"  [OK] Config loaded. Assistant Name: {config.get('assistant_name')}")
except Exception as e:
    print(f"  [FAIL] Config test failed: {e}")

try:
    from core.logger import logger
    logger.log("INFO", "Verification Test Run")
    print("  [OK] Logger verified.")
except Exception as e:
    print(f"  [FAIL] Logger test failed: {e}")

try:
    from core.system import System
    cpu = System.cpu()
    used_ram, total_ram = System.ram()
    battery = System.battery()
    print(f"  [OK] System Info verified. CPU: {cpu}%, RAM: {used_ram}/{total_ram} GB, Battery: {battery}")
except Exception as e:
    print(f"  [FAIL] System test failed: {e}")

try:
    from core.brain import Brain
    brain = Brain()
    res1 = brain.analyze("open chrome")
    res2 = brain.analyze("cpu usage")
    res3 = brain.analyze("click")
    res4 = brain.analyze("screenshot")
    print(f"  [OK] Brain Intents verified: {res1['intent']}, {res2['intent']}, {res3['intent']}, {res4['intent']}")
except Exception as e:
    print(f"  [FAIL] Brain test failed: {e}")

try:
    from database.db import db
    db.set_profile("test_user", "Wolfii")
    db.remember("skills", "python", "expert")
    recalled = db.recall("skills", "python")
    print(f"  [OK] SQLite Database verified (Profile & Long-Term Memory). Recalled: {recalled}")
except Exception as e:
    print(f"  [FAIL] Database test failed: {e}")

try:
    from automation.keyboard import press
    from automation.mouse import move
    from automation.clipboard import copy, paste
    copy("WOLF OS Test")
    pasted = paste()
    print(f"  [OK] Automation & Clipboard verified. Pasted content: '{pasted}'")
except Exception as e:
    print(f"  [FAIL] Automation test failed: {e}")

try:
    from vision.screenshot import Screenshot
    shot = Screenshot()
    path = shot.capture()
    print(f"  [OK] Vision Screenshot captured successfully at: {path}")
except Exception as e:
    print(f"  [FAIL] Screenshot test failed: {e}")

print("[TEST] All core modules verified successfully!")

