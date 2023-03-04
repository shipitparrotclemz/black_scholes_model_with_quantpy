# Black Scholes Model Implementation in Python

In this tutorial, we watched Jonathan, founder of Quantpy implement the Black Scholes Model here.

Black-Scholes Implementation in Python
- https://www.youtube.com/watch?v=FzeXWMlTDHY&ab_channel=QuantPy

In a bid to learn from Jonathan about the Black Scholes Model, we implemented a service here, responsible for calculating the fair price of an European Call / Put option here.

### Watch us build this up on Youtube here!

Watch me watch Quantpy Implement the Black Scholes Model
- https://www.youtube.com/watch?v=ATjOxtb5YC4&ab_channel=ShipItParrot

### Install dependencies

We are using 
- python3.9
- scipy for `scipy.stats.norm.cdf` (the black scholes formula uses the cumulative distribution function of the standard normal distribution)
- numpy for `np.log` (the black scholes formula uses the natural logarithm and the square root function)


```bash
virtualenv venv -p $(python3.9)
source venv/bin/activate
pip install -r requirements.txt
```

### Get the fair price of an European Call / Put option

Change the parameters in `app.py` and run the script.

```bash
python app.py
```

### Check for type errors with mypy

```commandline
dmypy run
```

### What is the Black Scholes Model?

The Black-Scholes model is a mathematical formula that is widely used to estimate the fair price of European-style options. The assumptions of the Black-Scholes model are as follows:

1. The underlying asset follows a log-normal distribution: The model assumes that the price of the underlying asset follows a log-normal distribution, meaning that its returns are normally distributed.

2. The option is European-style: The model assumes that the option can only be exercised at expiration, and not before.

3. There are no transaction costs: The model assumes that there are no transaction costs, such as commissions or fees, associated with buying or selling the option.

4. The risk-free interest rate is constant: The model assumes that the risk-free interest rate is constant throughout the life of the option.

5. The underlying asset has no dividends: The model assumes that the underlying asset does not pay any dividends during the life of the option.

6. There are no restrictions on short selling: The model assumes that it is possible to short sell the underlying asset without any restrictions.

7. The markets are efficient: The model assumes that the markets are efficient and that all relevant information is reflected in the price of the underlying asset.

These assumptions may not hold in real-world situations and that the Black-Scholes model is only an estimation tool. 

We should always consider the limitations and risks associated with any financial model, including this one.

### Now our smart parrots might ask:

Q: How do quantitative finance firms adjust the black scholes model to use it in normal market environments? the assumptions above are definitely not constant

Great question!

Here are some common adjustments (note that they are not exhaustive!):

1. Incorporating dividend payments: The Black-Scholes model assumes that the underlying asset does not pay any dividends. However, in reality, many assets do pay dividends. To account for this, the model can be adjusted by subtracting the present value of expected dividend payments from the current price of the underlying asset.

2. Factoring in transaction costs: The Black-Scholes model assumes no transaction costs, but in reality, buying and selling options comes with costs. To account for this, the model can be adjusted by incorporating estimates of transaction costs.

3. Adjusting for interest rate changes: The Black-Scholes model assumes that the risk-free interest rate is constant. However, interest rates can and do change. To account for this, the model can be adjusted to incorporate expected changes in interest rates.

4. Incorporating volatility skew: The Black-Scholes model assumes that volatility is constant across all strikes and expirations. However, in reality, the implied volatility of options can vary depending on their strike prices and expiration dates. This volatility skew can be incorporated into the model to improve its accuracy.

5. Using more complex models: The Black-Scholes model is a relatively simple model that assumes certain market conditions. However, more complex models, such as the binomial model or Monte Carlo simulations, can be used to more accurately reflect market realities.

In this repository, we have yet to adjust the model for such conditions, but we will be exploring that soon!

### References

For more information on the Black Scholes Model, check out these two sources!

1. IPOHub - The Black-Scholes Model - Brett Bartholomew
- https://www.ipohub.org/the-black-scholes-model/#:~:text=One%20component%20of%20the%20Black,the%20value%20of%20an%20option.

2. Investopedia - Black-Scholes Model: What It Is, How It Works, Options Formula - Adam Hayes
- https://www.investopedia.com/terms/b/blackscholes.asp