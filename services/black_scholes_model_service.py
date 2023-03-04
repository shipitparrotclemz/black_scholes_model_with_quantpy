from abc import ABC, abstractmethod

import numpy as np
from scipy.stats import norm

from models.option_enum import OptionEnum


class BlackScholesService(ABC):
    """
    Service responsible for calculating the fair price of a given european call / put option

    We can have multiple implementations for this, so we make this abstract
    We can extend off this ABC to implement a new variant
    """

    @staticmethod
    @abstractmethod
    def calculate(
        risk_free_interest_rate: float,  # 0.01
        current_stock_price: float,  # 30.00
        strike_price: float,  # 40.00
        time_to_expiry: float,  # 240/365
        volatility: float,  # 0.30
        option_type: OptionEnum,  # call / put
    ) -> float:
        """
        Used to calculate the fair price of a given european call / put option
        """
        raise NotImplementedError


class BlackScholesServiceImpl(BlackScholesService):
    @staticmethod
    def discounted_strike_price(
        strike_price: float,  # 40.00
        risk_free_interest_rate: float,  # 0.01
        time_to_expiry: float,  # 240/365
    ) -> float:
        """
        Calculates the discounted strike price given the risk free interest rate and time to expiry
        Q: Why is it that the strike price is discounted with respect to time_to_expiry
        A: Because the strike price is paid at the end of the option's life;
        - If we exercise the option at e.g 40 euros in 1 year
        - The 40 euros later, can be counted as worth 38 euros today.

        Q: How does the discounted strike price change if time_to_expiry increases
        A: The discounted strike price decreases

        Given the following variables:
        K: float = 40   # strike price, Euros
        r: float = 0.01 # risk free interest rate, 1 percent

        strike_price: 40
        discounted_strike_price if expire in 100 days: 39.89056094387437
        discounted_strike_price if expire in 200 days: 39.78142131042389

        Q: What is the intuition behind why the discounted strike price decreases with increasing time_to_expiry:
        A: If the option is exercised in a longer time, we will get 40 dollars with a lower amount (discounted strike price)
        if we get the risk free interest rate for the time we have to wait

        Q: Why is it that the strike price is discounted with respect to risk_free_interest_rate
        A: Because the strike price is paid at the end of the option's life;
        - If we exercise the option at e.g 40 euros in 1 year
        - The 40 euros later, can be counted as worth 40 euros today, but with a 1 percent interest rate

        Q: How does the discounted strike price change if risk_free_interest_rate increases
        A: The discounted strike price decreases

        Given the following variables:
        K: float = 40  # strike price, Euros
        T: float = 240 / 375  # options time to expiry, days divided by 365 days

        strike_price: 40
        discounted_strike_price at 1 percent: 39.74481745516596
        discounted_strike_price at 10 percent: 37.520199981229176

        Q: What is the intuition behind why the discounted strike price decreases with increasing risk_free_interest_rate:
        A: If the risk free interest rate is higher, we will get 40 dollars with a lower amount (discounted strike price)
        if we loan out the money we have for exercising the option, for the time we have to wait
        """
        return strike_price * np.exp(-risk_free_interest_rate * time_to_expiry)

    @staticmethod
    def calculate(
        risk_free_interest_rate: float,  # 0.01
        current_stock_price: float,  # 30.00
        strike_price: float,  # 40.00
        time_to_expiry: float,  # 240/365
        volatility: float,  # 0.30
        option_type: OptionEnum,  # call / put
    ) -> float:
        # d1 is the "time term" of the black scholes model
        # contains current_stock_price, risk_free_interest_rate, volatility, time_to_expiry
        # and they are technically related to time
        # TODO: understand what exactly this term means
        nat_log_current_price_to_strike_price: float = np.log(
            current_stock_price / strike_price
        )
        d1_numerator: float = (
            nat_log_current_price_to_strike_price
            + (risk_free_interest_rate + ((volatility ** 2) / 2)) * time_to_expiry
        )
        d1_denominator: float = volatility * np.sqrt(time_to_expiry)
        d1: float = d1_numerator / d1_denominator

        # d2 is the "volatility term" of the black scholes model
        d2: float = d1 - volatility * np.sqrt(time_to_expiry)

        price: float
        discounted_strike_price: float = (
            BlackScholesServiceImpl.discounted_strike_price(
                strike_price=strike_price,
                risk_free_interest_rate=risk_free_interest_rate,
                time_to_expiry=time_to_expiry,
            )
        )
        if option_type == OptionEnum.CALL:
            # loc is the mean of the normal distribution cdf -> 0
            # scale is the standard deviation of the normal distribution cdf -> 1
            price = current_stock_price * norm.cdf(
                d1, loc=0, scale=1
            ) - discounted_strike_price * norm.cdf(d2, loc=0, scale=1)
        elif option_type == OptionEnum.PUT:
            price = discounted_strike_price * norm.cdf(
                -d2, loc=0, scale=1
            ) - current_stock_price * norm.cdf(-d1, loc=0, scale=1)
        else:
            raise ValueError(f"Invalid option type: {option_type}")

        return price
