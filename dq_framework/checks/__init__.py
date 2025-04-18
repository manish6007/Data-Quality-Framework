from .completeness import CompletenessCheck
from .accuracy import AccuracyCheck
from .consistency import ConsistencyCheck
from .timeliness import TimelinessCheck
from .uniqueness import UniquenessCheck

CHECK_TYPE_MAP = {
    "completeness": CompletenessCheck,
    "accuracy": AccuracyCheck,
    "consistency": ConsistencyCheck,
    "timeliness": TimelinessCheck,
    "uniqueness": UniquenessCheck,
}
