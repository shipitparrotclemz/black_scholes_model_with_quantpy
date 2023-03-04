"""
Credits to Jonathan from QuantPy

Please watch his video here 
- https://www.youtube.com/watch?v=FzeXWMlTDHY&ab_channel=QuantPy
"""
from models.option_enum import OptionEnum
from services.black_scholes_model_service import BlackScholesServiceImpl

if __name__ == "__main__":
    # define variales
    r: float = 0.01  # risk free rate, interests for lending money to US treasury
    S: float = 30  # current stock price, Euros
    K: float = 40  # strike price, Euros
    T: float = 240 / 365  # options time to expiry, days divided by 365 days
    sigma: float = 0.30  # volatility. TODO: understand how this is derived

    # print(f"strike_price: {K}")
    #
    # discounted_strike_price_expiring_in_100_days: float = BlackScholesServiceImpl.discounted_strike_price(
    #     strike_price=K,
    #     risk_free_interest_rate=r,
    #     time_to_expiry=100/365
    # )
    #
    # print(f"discounted_strike_price if expire in 100 days: {discounted_strike_price_expiring_in_100_days}")
    #
    # discounted_strike_price_expiring_in_200_days: float = BlackScholesServiceImpl.discounted_strike_price(
    #     strike_price=K,
    #     risk_free_interest_rate=0.01,
    #     time_to_expiry=200/365
    # )
    #
    # print(f"discounted_strike_price if expire in 200 days: {discounted_strike_price_expiring_in_200_days}")

    # calculate the fair price of the call option
    fair_price_of_call_option: float = BlackScholesServiceImpl.calculate(
        risk_free_interest_rate=r,
        current_stock_price=S,
        strike_price=K,
        time_to_expiry=T,
        volatility=sigma,
        option_type=OptionEnum.CALL
    )

    # expected: 0.51
    print(f"fair_price of call option: {round(fair_price_of_call_option, 2)}")

    # calculate the fair price of the put option
    fair_price_of_put_option: float = BlackScholesServiceImpl.calculate(
        risk_free_interest_rate=r,
        current_stock_price=S,
        strike_price=K,
        time_to_expiry=T,
        volatility=sigma,
        option_type=OptionEnum.PUT
    )

    # expected: 10.25
    print(f"fair_price of put option: {round(fair_price_of_put_option, 2)}")