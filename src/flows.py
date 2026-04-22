from prefect import flow, task
import subprocess

@task
def run_generator():
    subprocess.run(["python", "src/generator.py"], check=True)

@flow(name="Resumex Generation Flow")
def main_flow():
    run_generator()

if __name__ == "__main__":
    main_flow()