import simpy
import random
import numpy


class carWash():
    def __init__(self,entorno,maquinas):
        self.env = entorno
        self.maquinas = simpy.Resource(entorno, maquinas)

    def llegada_maquina(self,tiempo):
        yield self.env.timeout(tiempo)

    def lavado_vehiculo(self,tiempo):
        yield self.env.timeout(tiempo)

    def salida_vehiculo(self,tiempo):
        yield self.env.timeout(tiempo)

    def llegada_vehiculo(self,vehiculo):
        print('llega {} a la hora {:,.2f}'.format(vehiculo, self.env.now))
        with self.maquinas.request() as maquina:
            yield maquina
            #proceso de llegar a la maquina
            tiempo_llegada = random.randint(1,3)
            print('El {} seb traslada a la maquina a la hora {:,.2f}'.format(vehiculo,self.env.now))
            yield self.env.process(self.llegada_maquina(tiempo_llegada))
            print('el {} llego a la maquina a la hora {:,.2f}'.format(vehiculo,self.env.now))
            #proceso de lavado
            tiempo_lavado = random.randint(5, 11)
            yield self.env.process(self.lavado_vehiculo(tiempo_lavado))
            print('El {} se acabo de lavar a la hora {:,.2f}'.format(vehiculo,self.env.now))
            #proceso de salida del vehiculo
            tiempo_salida = random.randint(2, 6)
            print('El {} se traslada a la salida {:,.2f}'.format(vehiculo,self.env.now))
            yield self.env.process(self.salida_vehiculo(tiempo_salida))
            print('El {} salio a la hora {:,.2f}'.format(vehiculo,self.env.now))


        

        


class Simulacion():

    def __init__(self,inicio):
        self.inicio = inicio
        self.nombre_vehiculo = 'vehiculo_{}'
        


    def ejecutar_simulacion(self,env,maquinas,intervalo):
        car_wash = carWash(env, maquinas)
        self.iniciar_vehiculos(env, car_wash)

        while True:
            yield env.timeout(random.randint(intervalo-2,intervalo+2))
            self.inicio+=1
            yield env.process(car_wash.llegada_vehiculo(self.nombre_vehiculo.format(self.inicio)))

    def iniciar_vehiculos(self,env,car_wash):
        for i in range(self.inicio):
            env.process(car_wash.llegada_vehiculo(self.nombre_vehiculo.format(i)))



if __name__ == '__main__':

    inicio = 3
    maquinas = 3
    intervalo = 9
    tiempo_simulacion = 24

    env = simpy.Environment()
    simulacion = Simulacion(inicio)
    env.process(simulacion.ejecutar_simulacion(env, maquinas, intervalo))
    env.run(until=tiempo_simulacion)

