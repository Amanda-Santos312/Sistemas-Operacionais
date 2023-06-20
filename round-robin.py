class Processo(object):
    def __init__(self, id, execução, ingresso):
        self.id = id
        self.execução = execução  
        self.ingresso = ingresso 
        self.execução_tmp = execução
        self.espera = 0
        self.return_ = 0
        self.ending = 0

try:
    numero_processos = int(input('Quantidade de processos: '))
    print()
    if numero_processos > 0:
        lista_processos = []

        #pede as informações sobre os processos a serem executados
        for numero_p in range(numero_processos):
            ingresso_tmp = -1
            print(f'Processo {numero_p + 1}')
            while ingresso_tmp < 0:
                ingresso_tmp = int(input(f'Tempo de ingresso do processo {numero_p + 1}: '))

            execução_tmp = 0
            while execução_tmp < 1:
                execução_tmp = int(input(f'Tempo de execução do processo {numero_p + 1}: '))

            lista_processos.append(Processo(numero_p + 1, execução_tmp, ingresso_tmp))
            print('')

        quantum = 0
        while quantum < 1:
            quantum = int(input('Valor do quantum: '))
        quantum_tmp = quantum

        troca_contexto = 0
        while troca_contexto < 1:
            troca_contexto = int(input('Tempo de troca de contexto: '))

        def ordena_por_tempo_ingresso(lista):
            for proc in range(1, len(lista)):
                item = proc
                while item > 0 and lista[item].ingresso < lista[item-1].ingresso:
                    lista[item], lista[item-1] = lista[item-1], lista[item]
                    item = item - 1
            return lista

        lista_processos = ordena_por_tempo_ingresso(lista_processos)  

        mirror_processos = len(lista_processos)

        time = 0
        tail_processos = [] #armazena processos de acordo com o ingresso
        context_switches = 0 #trocas de contexto
        currently_execution_process = None  # Processo em execução
        next_processos = 0  # Próximo

        print()
        print()
        print('Round Robin em execução')
        while mirror_processos > 0:
            print(f'\n----- Tempo: {time} -----')
            #verifica se o processo é o próximo a entrar na fila de pronto
            if len(lista_processos) > next_processos and time >= lista_processos[next_processos].ingresso:
                print(f'O processo {lista_processos[next_processos].id} ingressou na fila de pronto')
                tail_processos.append(lista_processos[next_processos])
                next_processos += 1
                
            else: #se já estiver na fila, 
                if next_processos > 0 or len(tail_processos) > 0:
                    if currently_execution_process is None: #ele retira da tail_processos para que seja executado
                        currently_execution_process = tail_processos.pop(0)
                        print(f'O processo {currently_execution_process.id} sai da fila e executa')

                    if currently_execution_process.execução_tmp >= quantum:#retira da execução o quantum
                        currently_execution_process.execução_tmp -= quantum
                        print(f'Tira-se {quantum} unidades de tempo da execução do processo {currently_execution_process.id}')
                        time += quantum
                    else:#se a execução for menor que o quantum tira exatamente o tempo de execução
                        time += currently_execution_process.execução_tmp
                        print(f'Tira-se {currently_execution_process.execução_tmp} unidades de tempo da execução do processo {currently_execution_process.id}')
                        currently_execution_process.execução_tmp = 0
                        #atualização do processo
                    if currently_execution_process.execução_tmp < 1: 
                        print(f' ----- Tempo: {time} -----')
                        print(f'O processo {currently_execution_process.id} foi executado e finalizado.')
                        currently_execution_process.ending = time
                        currently_execution_process.return_ = currently_execution_process.ending - currently_execution_process.ingresso #tempo total de execução do processo
                        currently_execution_process.espera = currently_execution_process.return_ - currently_execution_process.execução - currently_execution_process.ingresso #tempo total de espera do processo
                        mirror_processos -= 1
                        currently_execution_process = None
                    else: #momento de troca de contexto
                        tail_processos.append(currently_execution_process)
                        print(f'O processo {currently_execution_process.id} volta à fila de pronto')
                        currently_execution_process = None
                    context_switches += 1 #incrementa a quantidade de trocas de contexto
                    time += troca_contexto
                else:
                    time += 1
        time += 1
        print()
        print('Algoritmo finalizado!')
        print()
        print('RESULTADOS')
        print()
        total_return = 0
        total_espera = 0
        for processo in lista_processos:
            print(f'Processo {processo.id}, finalizou: {processo.ending}, tempo de espera: {processo.espera}, retorno: {processo.return_}')
            total_return += processo.return_
            total_espera += processo.espera

        print(f'Total de trocas de contexto: {context_switches}')
        print(f'Tempo total de execução do Round Robin: {time-troca_contexto}')
        print(f'Tempo médio de vida: {total_return / len(lista_processos)}')
        print(f'Tempo médio de espera: {total_espera / len(lista_processos)}')
        print()

    else:
        print('Digite um valor maior que 0.')

except Exception as e:
    print(e)
       