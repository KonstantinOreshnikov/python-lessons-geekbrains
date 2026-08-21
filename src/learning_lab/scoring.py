"""Small, domain-neutral scoring example used by the learning lab."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Activity:
    """Represent one planned activity and its observed result."""

    name: str
    planned_minutes: int
    actual_minutes: int
    completed: bool

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must not be blank")
        if self.planned_minutes < 0 or self.actual_minutes < 0:
            raise ValueError("minutes must not be negative")


def activity_score(activity: Activity) -> float:
    """Return a score from 0 to 100 for one activity."""
    if not activity.completed:
        return 0.0
    if activity.planned_minutes == 0:
        return 100.0
    return round(min(activity.actual_minutes / activity.planned_minutes, 1.0) * 100, 2)


def daily_score(activities: list[Activity]) -> float:
    """Return the arithmetic mean score, or zero for an empty day."""
    if not activities:
        return 0.0
    return round(sum(map(activity_score, activities)) / len(activities), 2)
