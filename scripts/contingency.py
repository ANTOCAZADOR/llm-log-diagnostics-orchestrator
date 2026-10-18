from prefect import flow, task


@task
def notify_team(service: str, severity: str):
    print(f"[TASK] Notifying the on-call team. Service: {service} | Severity: {severity}")
    return True


@task
def restart_service(service: str):
    print(f"[TASK] Executing restart commands for the {service} container...")
    return "Reset complete. Service is back online."


@flow(name="Automatic Service Recovery", log_prints=True)
def contingency_orchestrator(service: str = "api_payments", severity: str = "critical"):
    print(f"[PROCESS INITIATED] Responding to an incident involving {service}")

    notify_team(service, severity)
    result = restart_service(service)

    print(f"[PROCESS COMPLETED] System status: {result}")


if __name__ == "__main__":
    contingency_orchestrator()