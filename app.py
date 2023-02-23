import flask
import jaeger_client

config = jaeger_client.Config(
    config={
        'sampler': {'type': 'const', 'param': True}, 'logging': True,
    },
    service_name='my-app',
)

tracer = config.initialize_tracer()

app = flask.Flask(__name__)

@app.route('/')
def index():
    with tracer.start_span('tracing') as span:
        span.log_kv({'message': 'checking tracing'})
        return 'Hello World!'

app.run()

