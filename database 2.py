from typing import TypedDict, Optional, Required, NotRequired, Literal
from pydantic import TypeAdapter

# Student schema, this defines how the student_profiles is to be structured
StudentSchema: TypedDict = TypedDict("StudentSchema", {
    "name": str,
    "matric": str,
    "age": int,
    "cgpa": float,
    "is_active": bool,
    "courses": Optional[list[str]],
    "departmentInfo": Optional[tuple[str, str, int]]
})

type gradeType = Literal['A', 'B', 'C', 'D', 'F']

ResultSchema: TypedDict = TypedDict("ResultSchema", {
    "matric": Required[Optional[str]], # could be of type str or None
    "courses": Required[list[str]],
    "scores": Required[list[int]],
    "grades": NotRequired[list[gradeType]]
})

type StudentProfilesSchema = list[StudentSchema]
type StudentResultsSchema = list[ResultSchema]

# Data of the students
courses: list[str] = ["ELE311", "ELE21", "ELE331", "ELE361"]
student_names: list[str] = []

student_profiles: list[StudentSchema] = [
    {
        "name": "Abdulazeez",
        "matric": "22/30GC097",
        "age": 20,
        "cgpa": 4.6,
        "is_active": True,
        "courses": courses,
        "departmentInfo": ("Electrical/Electronics", "Faculty of Engineering", 2025)
    },
    {
        "name": "Gabriel",
        "matric": "22/30GC098",
        "age": 38,
        "cgpa": 2.1,
        "is_active": True,
        "courses": courses,
        "departmentInfo": ("Electrical/Electronics", "Faculty of Engineering", 2025)
    },
    {
        "name": "Yusuf",
        "matric": "22/30GC086",
        "age": 23,
        "cgpa": 3.2,
        "is_active": True,
        "courses": courses,
        "departmentInfo": ("Electrical/Electronics", "Faculty of Engineering", 2025)
    },
    {
        "name": "Tammy",
        "matric": "22/30GC076",
        "age": 25,
        "cgpa": 3.5,
        "is_active": True,
        "courses": courses,
        "departmentInfo": ("Electrical/Electronics", "Faculty of Engineering", 2025)
    },
    {
        "name": "James",
        "matric": "22/30GC122",
        "age": 19,
        "cgpa": 3.2,
        "is_active": True,
        "courses": courses,
        "departmentInfo": ("Electrical/Electronics", "Faculty of Engineering", 2025)
    }
]

student_results: list[ResultSchema] = [
    {
        "matric": "22/30GC097",
        "courses": courses,
        "scores": [10, 30, 53, 87]
    },
    {
        "matric": "20/89AC098",
        "courses": courses,
        "scores": [10, 30, 53, 87]
    },
    {
        "matric": "20/60AC086",
        "courses": courses,
        "scores": [49, 18, 74, 62]
    },
    {
        "matric": "20/60AC122",
        "courses": courses,
        "scores": [40, 89, 77, 32]
    },
    {
        "matric": "20/60AC076",
        "courses": courses,
        "scores": [18, 52, 67, 90]
    }
]

student_validator: TypeAdapter = TypeAdapter(StudentProfilesSchema)
student_profiles: list[StudentSchema] = student_validator.validate_python(student_profiles)

result_validator: TypeAdapter = TypeAdapter(StudentResultsSchema)
student_results: list[ResultSchema] = result_validator.validate_python(student_results)

