from banking.pipeline.pipeline import Pipeline
from banking.exception import BankingException
from banking.logger import logging
from banking.config.configuration import Configuartion
from banking.components.data_transformation import DataTransformation
import os


def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuartion(config_file_path=config_path))
        #pipeline.run_pipeline()
        pipeline.run_pipeline()
        logging.info("main function execution completed.")


    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()
