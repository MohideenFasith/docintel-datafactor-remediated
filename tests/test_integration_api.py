from __future__ import annotations


def test_document_lifecycle_is_exercised_through_http(client) -> None:
    created = client.post(
        "/v1/documents",
        headers={"x-actor": "integration-user"},
        json={
            "title": "Quarterly invoice",
            "content": "Cloud hosting invoice USD 4200 for August 2026.",
            "source": "integration",
            "tags": ["finance", "cloud"],
        },
    )
    assert created.status_code == 201
    document_id = created.json()["id"]

    fetched = client.get(f"/v1/documents/{document_id}")
    assert fetched.status_code == 200
    assert fetched.json()["title"] == "Quarterly invoice"

    search = client.get("/v1/search", params={"q": "cloud invoice"})
    assert search.status_code == 200
    assert search.json()["total"] >= 1
    assert search.json()["hits"][0]["document_id"] == document_id

    patched = client.patch(
        f"/v1/documents/{document_id}",
        json={"title": "Revised quarterly invoice", "tags": ["finance", "reviewed"]},
    )
    assert patched.status_code == 200
    assert "reviewed" in patched.json()["tags"]

    deleted = client.delete(f"/v1/documents/{document_id}")
    assert deleted.status_code == 204
    assert client.get(f"/v1/documents/{document_id}").status_code == 404

# _ref-94534

# _ref-52989

# _ref-16482

# _ref-67092

# _ref-81176

# _ref-13472

# _ref-28218

# _ref-98780

# _ref-84977

# _ref-63174

# _ref-83129

# _ref-28643

# _ref-58345

# _ref-96972

# _ref-76650

# _ref-59743

# _ref-67391

# _ref-31780

# _ref-53420

# _ref-30961

# _ref-46071

# _ref-78774

# _ref-45842

# _ref-76333

# _ref-98026

# _ref-82223

# _ref-30362

# _ref-19272

# _ref-52028

# _ref-21147

# _ref-78506

# _ref-77621

# _ref-17960

# _ref-84240

# _ref-58633

# _ref-12911
