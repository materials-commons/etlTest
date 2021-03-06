import os
import logging
import sys
import configparser
from etl.etlworker import ETLWorker

user_endpoint_config_file_path = os.path.join('.globus_test', 'endpoint.ini')
config_file_locaton_for_user_endpoint = os.path.join(os.path.expanduser("~"), user_endpoint_config_file_path)


def main():

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)

    log = logging.getLogger('elt.run_worker_once')

    config = configparser.ConfigParser()
    config.read(str(config_file_locaton_for_user_endpoint))

    user_id = "test@test.mc"
    project_id = "3751239e-c0eb-4af2-ae33-a89d1911b968"
    experiment_name = "Test from excel"
    experiment_description = "An experiment built via etl from test data"
    globus_endpoint = config['test']['endpoint']
    endpoint_path = config['test']['directory']
    request_uuid = project_id
    excel_file_relative_path = "input.xlsx"
    data_dir_relitive_path = "data"

    log.info("user_id = " + user_id)
    log.info("project_id = " + project_id)
    log.info("experiment_name = " + experiment_name)
    log.info("experiment_description = " + experiment_description)
    log.info("globus_endpoint = " + globus_endpoint)
    log.info("endpoint_path = " + endpoint_path)
    log.info("request_uuid = " + request_uuid)
    log.info("excel_file_relative_path = " + excel_file_relative_path)
    log.info("data_dir_relitive_path = " + data_dir_relitive_path)

    worker = ETLWorker(user_id)
    worker.run_with(project_id, experiment_name, experiment_description,
                    globus_endpoint, endpoint_path, request_uuid,
                    excel_file_relative_path, data_dir_relitive_path)


if __name__ == "__main__":
    main()