import pytest

from learning_lab.scoring import Activity, activity_score, daily_score


def test_completed_activity_is_capped_at_100() -> None:
    activity = Activity("Study", planned_minutes=30, actual_minutes=45, completed=True)
    assert activity_score(activity) == 100.0


def test_incomplete_activity_scores_zero() -> None:
    activity = Activity("Exercise", planned_minutes=30, actual_minutes=30, completed=False)
    assert activity_score(activity) == 0.0


def test_daily_score_averages_activities() -> None:
    activities = [
        Activity("Study", 60, 30, True),
        Activity("Exercise", 30, 30, True),
    ]
    assert daily_score(activities) == 75.0


def test_negative_minutes_are_rejected() -> None:
    with pytest.raises(ValueError, match="negative"):
        Activity("Study", planned_minutes=-1, actual_minutes=0, completed=False)
