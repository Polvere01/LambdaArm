import time

def lambda_handler(event, context):
    start_time = time.time()  # Tempo inicial

    # Exemplo de algoritmo: calcular números Fibonacci
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    # Executa o algoritmo
    result = fibonacci(39)  # Você pode ajustar este número conforme necessário

    end_time = time.time()  # Tempo final
    duration = end_time - start_time  # Duração da execução

    # Logging com CloudWatch
    print(f'Resultado: {result}, Tempo de execução: {duration} segundos')

    return {
        'statusCode': 200,
        'body': f'Resultado: {result}, Tempo de execução: {duration} segundos'
    }

