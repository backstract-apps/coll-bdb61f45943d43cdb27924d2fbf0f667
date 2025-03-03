from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_users(db: Session):

    users_all = db.query(models.Users).all()
    users_all = [new_data.to_dict() for new_data in users_all] if users_all else users_all

    res = {
        'users_all': users_all,
    }
    return res

async def get_users_user_id(db: Session, user_id: int):

    users_one = db.query(models.Users).filter(models.Users.user_id == user_id).first() 
    users_one = users_one.to_dict() if users_one else users_one

    res = {
        'users_one': users_one,
    }
    return res

async def post_users(db: Session, raw_data: schemas.PostUsers):
    user_id:str = raw_data.user_id
    first_name:str = raw_data.first_name
    last_name:str = raw_data.last_name
    email:str = raw_data.email
    phone_number:str = raw_data.phone_number
    role:str = raw_data.role


    record_to_be_added = {'user_id': user_id, 'first_name': first_name, 'last_name': last_name, 'email': email, 'phone_number': phone_number, 'role': role}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    res = {
        'users_inserted_record': users_inserted_record,
    }
    return res

async def put_users_user_id(db: Session, raw_data: schemas.PutUsersUserId):
    user_id:str = raw_data.user_id
    first_name:str = raw_data.first_name
    last_name:str = raw_data.last_name
    email:str = raw_data.email
    phone_number:str = raw_data.phone_number
    role:str = raw_data.role


    users_edited_record = db.query(models.Users).filter(models.Users.user_id == user_id).first()
    for key, value in {'user_id': user_id, 'first_name': first_name, 'last_name': last_name, 'email': email, 'phone_number': phone_number, 'role': role}.items():
          setattr(users_edited_record, key, value)
    db.commit()
    db.refresh(users_edited_record)
    users_edited_record = users_edited_record.to_dict() 

    res = {
        'users_edited_record': users_edited_record,
    }
    return res

async def delete_users_user_id(db: Session, user_id: int):

    users_deleted = None
    record_to_delete = db.query(models.Users).filter(models.Users.user_id == user_id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict() 

    res = {
        'users_deleted': users_deleted,
    }
    return res

