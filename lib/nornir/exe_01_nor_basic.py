from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

from nornir import InitNornir

nr = InitNornir(
    config_file="config.yaml", dry_run=True
)

results = nr.run(
    task=napalm_get, getters=["facts", "interfaces"]
)
print_result(results)
