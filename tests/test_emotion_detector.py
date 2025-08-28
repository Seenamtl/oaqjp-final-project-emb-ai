import importlib
import os
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_blank_returns_400():
    
    mod = importlib.import_module("app.emotion_detector")
    res = mod.emotion_detector("   ")
    assert res.status_code == 400
    assert res.dominant == ""

def test_sentence_format_success(monkeypatch):
    
    os.environ["WATSON_EMOTION_ENDPOINT"] = "https://example.com/api"

    
    mod = importlib.import_module("app.emotion_detector")
    mod = importlib.reload(mod)

    
    def fake_call(_):
        return 200, {"joy": 0.9, "sadness": 0.1}
    monkeypatch.setattr(mod, "_call_watson_api", fake_call)

    msg, code = mod.emotion_sentence("Great news!")
    assert code == 200
    assert msg.strip().lower() == "the dominant emotion is joy."
