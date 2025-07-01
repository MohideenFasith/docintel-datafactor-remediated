
def test_collection_api_lifecycle(client):
    document = client.post("/v1/documents", json={"title": "A", "content": "collection content"}).json()
    created = client.post("/v1/collections", params={"name": "Research", "description": "Research docs"})
    assert created.status_code == 201
    collection_id = created.json()["id"]

    added = client.put(f"/v1/collections/{collection_id}/documents/{document['id']}")
    assert added.status_code == 200
    assert document["id"] in added.json()["document_ids"]

    listed = client.get("/v1/collections")
    assert listed.status_code == 200
    assert listed.json()[0]["name"] == "Research"

    removed = client.delete(f"/v1/collections/{collection_id}/documents/{document['id']}")
    assert removed.status_code == 200
    assert removed.json()["document_ids"] == []

    assert client.delete(f"/v1/collections/{collection_id}").status_code == 204
    assert client.get(f"/v1/collections/{collection_id}").status_code == 404


def test_collection_rejects_duplicate_names_and_missing_documents(client):
    assert client.post("/v1/collections", params={"name": "Ops"}).status_code == 201
    assert client.post("/v1/collections", params={"name": "ops"}).status_code == 409
    collection_id = client.get("/v1/collections").json()[0]["id"]
    assert client.put(f"/v1/collections/{collection_id}/documents/missing").status_code == 404

# _ref-55156

# _ref-46050

# _ref-90101

# _ref-78238

# _ref-58927

# _ref-10690

# _ref-61591

# _ref-42250

# _ref-27275

# _ref-45475

# _ref-48391

# _ref-36430

# _ref-15133

# _ref-69759

# _ref-46514

# _ref-93872
