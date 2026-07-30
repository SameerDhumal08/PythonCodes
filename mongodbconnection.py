from beanie import Document, init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

# Define Document (Model)
class Employee(Document):
    name: str
    age: int
    department: str

    class Settings:
        name = "employees"  # Collection name


async def init_db():
    # Connect to MongoDB
    client = AsyncIOMotorClient("mongodb://localhost:27017")

    # Initialize Beanie
    await init_beanie(
        database=client.employee_db,
        document_models=[Employee]
    )


async def main():
    await init_db()

    # Insert document
    employee = Employee(
        name="Sameer",
        age=26,
        department="IT"
    )

    await employee.insert()

    print("Employee inserted successfully!")

    # Fetch all employees
    employees = await Employee.find_all().to_list()

    for emp in employees:
        print(emp)


asyncio.run(main())
