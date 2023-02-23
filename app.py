from flask import Flask
from opentracing import Tracer
from jaeger_client import Config

config = Config(
    config={
        'sampler': {'type': 'const', 'param': 1}, 'logging': True,
    },
    service_name='my-app',
)

tracer = config.initialize_tracer()

app = Flask(__name__)

@app.route('/')
def index():
    with tracer.start_span('tracing') as span:
        span.log_kv({'message': 'checking tracing'})
        return 'Hello World!'


app.run()

