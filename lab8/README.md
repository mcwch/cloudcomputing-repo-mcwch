# Lab 8: Simulating Basic Load Balancing with Flask

## Overview

This lab simulates a basic load balancer using Flask. Two backend Flask servers run on ports 5001 and 5002, while the load balancer runs on port 5000.

## Files

- `server1.py` - Backend Server 1 running on port 5001
- `server2.py` - Backend Server 2 running on port 5002
- `load_balancer.py` - Randomly redirects requests to one of the backend servers
- `requirements.txt` - Required Python libraries

## How the Load Balancer Works

The Flask load balancer runs on port 5000 and randomly selects one of two backend servers using `random.choice()`. It then redirects each request to Server 1 on port 5001 or Server 2 on port 5002.

## Observations

The requests were distributed between both backend servers. Since the selection was random, the requests did not alternate in a strict order, and one server sometimes received more requests than the other.

## Running the Application

Start the applications in three separate terminals:

- `python server1.py`
- `python server2.py`
- `python load_balancer.py`

Test the load balancer with:

`for i in {1..10}; do curl -s -L http://localhost:5000; echo; done`
