#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from tempfile import NamedTemporaryFile, TemporaryFile
from unittest import TestCase
from YamlObject import YamlObject
import yaml

__author__ = 'Marco Bartel'


class TestYamlObject(TestCase):
    def setUp(self):
        # generate temporary test yaml file
        self.file = NamedTemporaryFile(delete=False)
        self.file.write(b"""
# An employee record
name: Example Developer
job: Developer
skill: Elite
employed: True
foods:
    - Apple
    - Orange
    - Strawberry
    - Mango
languages:
    ruby: Elite
    python: Elite
    dotnet: Lame
games:
    strategy:
        realtime:
            - c&c
            - panzers
        """)
        self.file.close()
        self.obj = YamlObject.load(self.file.name)

    def doCleanups(self):
        os.unlink(self.file.name)

    def test_load(self):
        self.assertIsInstance(self.obj, YamlObject)

    def test_toDict(self):
        data = yaml.load(open(self.file.name).read())
        self.assertEqual(self.obj.toDict(), data)

    def test___dir__(self):
        dataList = list(yaml.load(open(self.file.name).read()).keys())
        dirList = dir(self.obj)
        self.assertTrue(all(key in dirList for key in dataList))

    def test_dynamicAccess(self):
        self.assertEqual(self.obj.languages.python, "Elite")
