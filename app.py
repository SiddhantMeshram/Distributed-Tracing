from flask import Flask
from opentracing import Tracer
from jaeger_client import Config

app = Flask(__name__)

# Initialize Jaeger tracer configuration
config = Config(
    config={
        'sampler': {'type': 'const', 'param': 1},
        'logging': True,
    },
    service_name='my-app',
)

# Initialize tracer instance with Jaeger configuration
tracer = config.initialize_tracer()

# Define a Flask route that creates a new span and returns a response
@app.route('/')
def index():
    with tracer.start_span('tracing') as span:
        span.log_kv({'event': 'tracing', 'message': 'checking tracing'})
        return 'Hello World!'

# Run the Flask application
if __name__ == '__main__':
    app.run()

