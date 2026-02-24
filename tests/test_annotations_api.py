
def test_annotations_api_lifecycle(client):
    document_id = client.post("/v1/documents", json={"title": "Review", "content": "annotation content"}).json()["id"]
    created = client.post(
        f"/v1/documents/{document_id}/annotations",
        json={"body": "Needs legal review", "labels": ["Legal", "legal", "urgent"]},
    )
    assert created.status_code == 201
    annotation_id = created.json()["id"]
    assert created.json()["labels"] == ["legal", "urgent"]

    listed = client.get(f"/v1/documents/{document_id}/annotations")
    assert listed.status_code == 200
    assert listed.json()[0]["id"] == annotation_id

    updated = client.patch(
        f"/v1/annotations/{annotation_id}",
        json={"body": "Reviewed", "labels": ["done"]},
    )
    assert updated.status_code == 200
    assert updated.json()["body"] == "Reviewed"
    assert updated.json()["labels"] == ["done"]

    assert client.delete(f"/v1/annotations/{annotation_id}").status_code == 204
    assert client.delete(f"/v1/annotations/{annotation_id}").status_code == 404


def test_annotations_require_existing_document(client):
    response = client.post("/v1/documents/missing/annotations", json={"body": "orphan"})
    assert response.status_code == 404
    assert client.get("/v1/documents/missing/annotations").status_code == 404

# _ref-24596

# _ref-44649

# _ref-17111

# _ref-57123

# _ref-32561

# _ref-59048

# _ref-88518

# _ref-90248

# _ref-94731

# _ref-19070

# _ref-97564

# _ref-39989

# _ref-53557

# _ref-30375

# _ref-59996

# _ref-45200

# _ref-67460

# _ref-14163

# _ref-66820

# _ref-80003

# _ref-60993

# _ref-11166

# _ref-44457

# _ref-60122

# _ref-52566

# _ref-97693

# _ref-15438

# _ref-55761

# _ref-15684

# _ref-75063

# _ref-85285
