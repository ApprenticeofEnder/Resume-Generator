from typing import Dict

from pydantic import BaseModel


class WebLink(BaseModel):
    link: str
    display: str


class BasicData(BaseModel):
    name: str
    email: WebLink
    website: WebLink
    github: WebLink


class Education(BaseModel):
    institution: str
    degree: str
    location: str
    start: str
    end: str


class Skills(BaseModel):
    programming_languages: list[str]
    frameworks: list[str]
    tools: list[str]


class Experience(BaseModel):
    title: str
    company: str
    start: str
    end: str
    location: str
    sar: list[str]


class Project(BaseModel):
    title: str
    stack: str
    start_year: str
    end_year: str
    sar: list[str]


class ResumeData(BaseModel):
    basic: BasicData
    education: list[Education]
    skills: Skills
    experience: list[Experience]
    projects: list[Project]
    volunteering: list[Experience]


class ResumeResponse(BaseModel):
    name: str
    resume_b64: str
