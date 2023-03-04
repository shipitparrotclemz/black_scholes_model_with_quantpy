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