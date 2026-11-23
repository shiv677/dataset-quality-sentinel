"""Dataset Quality Sentinel."""
try:
    from .models import DuplicateMatch, RecordAudit, SentinelReport
    from .sentinel import (
        DatasetQualitySentinel,
        DatasetSentinel,
        compute_sha256,
        compute_simhash,
        detect_corruption,
        hamming_distance,
        normalize_text,
        normalize_unicode,
    )
except (ImportError, ValueError):
    from models import DuplicateMatch, RecordAudit, SentinelReport
    from sentinel import (
        DatasetQualitySentinel,
        DatasetSentinel,
        compute_sha256,
        compute_simhash,
        detect_corruption,
        hamming_distance,
        normalize_text,
        normalize_unicode,
    )
