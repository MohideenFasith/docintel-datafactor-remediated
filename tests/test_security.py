import pytest

from docintel.errors import PermissionDenied, RateLimitExceeded
from docintel.security import ApiKeyAuthenticator, SlidingWindowRateLimiter


def test_authenticator_roles():
    auth = ApiKeyAuthenticator("writer-secret", "admin-secret")
    assert auth.authenticate("writer-secret").role == "writer"
    assert auth.authenticate("admin-secret").role == "admin"
    with pytest.raises(PermissionDenied):
        auth.authenticate("wrong")


def test_authenticator_open_mode_is_admin_for_self_contained_dev():
    assert ApiKeyAuthenticator().authenticate(None).role == "admin"


def test_role_requirement():
    principal = ApiKeyAuthenticator("key").authenticate("key")
    with pytest.raises(PermissionDenied):
        ApiKeyAuthenticator.require(principal, "admin")


def test_rate_limiter_window():
    limiter = SlidingWindowRateLimiter(limit=2, window_seconds=10)
    assert limiter.check("user", now=0) == 1
    assert limiter.check("user", now=1) == 0
    with pytest.raises(RateLimitExceeded):
        limiter.check("user", now=2)
    assert limiter.check("user", now=11) == 1

# _ref-89706

# _ref-71542

# _ref-93006

# _ref-44874

# _ref-43052

# _ref-13995

# _ref-20456

# _ref-81063

# _ref-78010

# _ref-82422

# _ref-42741

# _ref-32563

# _ref-95202

# _ref-97261

# _ref-74706

# _ref-11716

# _ref-76889

# _ref-20119

# _ref-55354

# _ref-24005

# _ref-61257

# _ref-24212

# _ref-30552

# _ref-22760

# _ref-68638

# _ref-37008

# _ref-85669

# _ref-30646
