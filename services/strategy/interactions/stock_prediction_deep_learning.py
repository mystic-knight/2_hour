import os
import secrets
import pandas as pd
from datetime import datetime

from services.strategy.models.stock_prediction import StockPrediction
from services.strategy.models.long_short_term_memory import LongShortTermMemory
from services.strategy.models.stock_data import StockData
from services.strategy.models.stock_prediction_plotter import Plotter
from services.strategy.models.stock_prediction_readme_generator import ReadmeGenerator

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))


def train_LSTM_network(stock):
    data = StockData(stock)
    # plotter = Plotter(True, stock.get_project_folder(), data.get_stock_short_name(), data.get_stock_currency(), stock.get_ticker())
    (x_train, y_train), (x_test, y_test), (training_data, test_data) = data.download_transform_to_numpy(stock.get_time_steps(), stock.get_project_folder())
    # plotter.plot_histogram_data_split(training_data, test_data, stock.get_validation_date())

    lstm = LongShortTermMemory(stock.get_project_folder())
    model = lstm.create_model(x_train)
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=lstm.get_defined_metrics())
    # history = model.fit(x_train, y_train, epochs=stock.get_epochs(), batch_size=stock.get_batch_size(), validation_data=(x_test, y_test),
    #                     callbacks=[lstm.get_callback()])
    # breakpoint()

    print("saving weights")
    # model.save(os.path.join(stock.get_project_folder(), 'model_weights.h5'))
    # un comment after some time

    # plotter.plot_loss(history)
    # plotter.plot_mse(history)

    print("display the content of the model")
    baseline_results = model.evaluate(x_test, y_test, verbose=2)
    for name, value in zip(model.metrics_names, baseline_results):
        print(name, ': ', value)

    print("plotting prediction results")
    test_predictions_baseline = model.predict(x_test)
    test_predictions_baseline = data.get_min_max().inverse_transform(test_predictions_baseline)
    test_predictions_baseline = pd.DataFrame(test_predictions_baseline)
    test_predictions_baseline.to_csv(os.path.join(stock.get_project_folder(), 'predictions.csv'))

    test_predictions_baseline.rename(columns={0: stock.get_ticker() + '_predicted'}, inplace=True)
    test_predictions_baseline = test_predictions_baseline.round(decimals=0)
    test_predictions_baseline.index = test_data.index
    # plotter.project_plot_predictions(test_predictions_baseline, test_data)

    generator = ReadmeGenerator(stock.get_github_url(), stock.get_token(), data.get_stock_short_name())
    generator.write()

    print("prediction is finished")

def stock_prediction_deep_learning(stoke_name = '^FTSE'):
    STOCK_TICKER = stoke_name
    STOCK_START_DATE = pd.to_datetime("2017-11-01")
    STOCK_VALIDATION_DATE = pd.to_datetime("2021-09-01")
    EPOCHS = int('100')
    BATCH_SIZE = int('10')
    TIME_STEPS = int('3')
    TODAY_RUN = datetime.today().strftime("%Y%m%d")
    TOKEN = STOCK_TICKER + '_' + TODAY_RUN + '_' + secrets.token_hex(16)
    GITHUB_URL = "https://github.com/saknius/"
    print('Ticker: ' + STOCK_TICKER)
    print('Start Date: ' + STOCK_START_DATE.strftime("%Y-%m-%d"))
    print('Validation Date: ' + STOCK_START_DATE.strftime("%Y-%m-%d"))
    print('Test Run Folder: ' + TOKEN)
    # create project run folder
    PROJECT_FOLDER = os.path.join(os.getcwd(), TOKEN)
    if not os.path.exists(PROJECT_FOLDER):
        os.makedirs(PROJECT_FOLDER)

    stock_prediction = StockPrediction(STOCK_TICKER, 
                                    STOCK_START_DATE, 
                                    STOCK_VALIDATION_DATE, 
                                    PROJECT_FOLDER, 
                                    GITHUB_URL,
                                    EPOCHS,
                                    TIME_STEPS,
                                    TOKEN,
                                    BATCH_SIZE)
    # Execute Deep Learning model
    train_LSTM_network(stock_prediction)