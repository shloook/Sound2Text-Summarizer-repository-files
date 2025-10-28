def test_import_pipeline():
    # A simple import smoke test
    import importlib
    mod = importlib.import_module("sound2text.pipeline")
    assert mod is not None
