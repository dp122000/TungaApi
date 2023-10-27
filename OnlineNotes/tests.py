from django.test import TestCase
import pytest
from TungaApi import app  # Import your API app instance (replace 'your_api' with the actual module name)
import json

# Create your tests here.

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# User Registration and Login Tests (8 points)
def test_user_registration(client):
    user_data = {
        "email": "patience@gmail.com",
        "first_name": "Patience",
        "last_name": "Ayo",
        "password": "patience"
    }
    response = client.post('/register', json=user_data)
    assert response.status_code == 201

def test_user_login(client):
    login_data = {
        "email": "patience@gmail.com",
        "password": "patience"
    }
    response = client.post('/login', json=login_data)
    assert response.status_code == 200

# User Logout Test 
def test_user_logout(client):
    response = client.post('/logout')
    assert response.status_code == 200

# Password Reset Tests (5 points)
def test_reset_password_request(client):
    reset_data = {
        "email": "patience@gmail.com"
    }
    response = client.post('/reset_password', json=reset_data)
    assert response.status_code == 200

def test_reset_password(client):
    reset_data = {
        "token": "valid_token",
        "new_password": "newpassword"
    }
    response = client.post('/reset_password/valid_token', json=reset_data)
    assert response.status_code == 200

# Diary Notes Tests 
# Add, view, update, and delete note tests go here
# Test adding a new note
def test_add_note(client):
    new_note_data = {
        "title": "Test Note",
        "content": "This is a test note."
    }
    response = client.post('/add_note', json=new_note_data, headers={"Authorization": f"Bearer"})
    assert response.status_code == 201

# Test viewing all notes for the authenticated user
def test_view_all_notes(client):
    response = client.get('/view_all_notes', headers={"Authorization": f"Bearer"})
    assert response.status_code == 200

# Test viewing a specific note
def test_view_specific_note(client):
    note_id = 1  # Replace with a valid note ID for an existing note
    response = client.get(f'/view_note/{note_id}', headers={"Authorization": f"Bearer"})
    assert response.status_code == 200

# Test updating a specific note
def test_update_note(client):
    note_id = 1  # Replace with a valid note ID for an existing note
    updated_note_data = {
        "title": "Updated Test Note",
        "content": "This is an updated test note."
    }
    response = client.put(f'/update_note/{note_id}', json=updated_note_data, headers={"Authorization": f"Bearer"})
    assert response.status_code == 200

# Test deleting a specific note
def test_delete_note(client):
    note_id = 1  # Replace with a valid note ID for an existing note
    response = client.delete(f'/delete_note/{note_id}', headers={"Authorization": f"Bearer"})
    assert response.status_code == 204


# Additional Diary Notes Tests
# Order, filter, sort, export, share, and set reminder tests go here
# Test ordering all notes by the latest
def test_order_notes_by_latest(client):
    response = client.get('/order_notes/latest', headers={"Authorization": f"Bearer"})
    assert response.status_code == 200

# Test filtering unfinished notes
def test_filter_unfinished_notes(client):
    response = client.get('/filter_notes/unfinished', headers={"Authorization": f"Bearer"})
    assert response.status_code == 200

# Test filtering overdue notes
def test_filter_overdue_notes(client):
    response = client.get('/filter_notes/overdue', headers={"Authorization": f"Bearer"})
    assert response.status_code == 200

# Test filtering done notes
def test_filter_done_notes(client):
    response = client.get('/filter_notes/done', headers={"Authorization": f"Bearer"})
    assert response.status_code == 200

# Test sorting notes by due date
def test_sort_notes_by_due_date(client):
    response = client.get('/sort_notes/due_date', headers={"Authorization": f"Bearer"})
    assert response.status_code == 200

# Test sorting notes by priority
def test_sort_notes_by_priority(client):
    response = client.get('/sort_notes/priority', headers={"Authorization": f"Bearer"})
    assert response.status_code == 200

# Test sorting notes by created time
def test_sort_notes_by_created_time(client):
    response = client.get('/sort_notes/created_time', headers={"Authorization": f"Bearer"})
    assert response.status_code == 200

# Test exporting notes to PDF
def test_export_notes_to_pdf(client):
    response = client.get('/export_notes/pdf', headers={"Authorization": f"Bearer"})
    assert response.status_code == 200

# Test exporting notes to CSV
def test_export_notes_to_csv(client):
    response = client.get('/export_notes/csv', headers={"Authorization": f"Bearer"})
    assert response.status_code == 200

# Test sharing or publishing notes via email
def test_share_notes_via_email(client):
    email_data = {
        "recipient_email": "recipient@example.com",
        "note_data": {
            "title": "Test Note",
            "content": "This is a test note."
        }
    }
    response = client.post('/share_notes/email', json=email_data, headers={"Authorization": f"Bearer"})
    assert response.status_code == 200

# Test setting an email reminder for a note
def test_set_email_reminder(client):
    note_id = 1  # Replace with a valid note ID for an existing note
    reminder_data = {
        "reminder_datetime": "2023-10-15 12:00:00"
    }
    response = client.post(f'/set_reminder/{note_id}', json=reminder_data, headers={"Authorization": f"Bearer"})
    assert response.status_code == 200

if __name__ == '__main__':
    pytest.main()
