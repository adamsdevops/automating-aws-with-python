# coding: utf-8
# imports boto3 and sets up a session and the s3 resource
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
