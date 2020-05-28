from ipykernel.kernelbase import Kernel
import irisnative

def get_iris_object():
    # Create connection to InterSystems IRIS
    connection = irisnative.createConnection('iris', 51773, 'IRISAPP', '_SYSTEM', 'SYS')

    # Create an iris object
    return irisnative.createIris(connection)


class ObjectScriptKernel(Kernel):
    implementation = 'object_script'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '1.0'
    banner = 'An ObjectScript kernel'
    language_info = {
        'name': 'Arbitrary',
        'mimetype': 'text/plain',
        'file_extension': '.cls',
    }

    def __init__(self, **kwargs):
        Kernel.__init__(self, **kwargs)
        self.iris = get_iris_object()

    def execute_code(self, code):
        class_name = "JupyterKernel.CodeExecutor"

        return self.iris.classMethodValue(class_name, "CodeResult", code)

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            codelines = code.split('\n')
            for codeline in codelines:
                execution_result = self.execute_code(codeline)
                if execution_result:
                    stream_content = {'name': 'stdout', 'text': execution_result}
                    self.send_response(self.iopub_socket, 'stream', stream_content)

        return {
            'status': 'ok',
            'execution_count': self.execution_count,
            'payload': [],
            'user_expressions': {},
        }


if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=ObjectScriptKernel)
