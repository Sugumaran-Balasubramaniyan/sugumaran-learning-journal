def test_project_imports():
    import app

    assert app.__file__ is not None


def test_parse_gtfs_time_after_midnight():
    from app.gtfs_import import parse_gtfs_time

    assert parse_gtfs_time("25:10:00") == 90600
