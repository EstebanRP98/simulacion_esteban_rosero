import papermill as pm
import argparse 

def main(fechas):
    pm.execute_notebook('Untitled.ipynb',
                    './out/output.ipynb',
                    parameters=dict(fecha_inicio=fechas[0],fecha_fin=fechas[1])
    )

if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument(
        'date',
        help='pasar fecha inicio y fin',
        type=str
    )

    arguments = args.parse_args()

    main([i for i in arguments.date.split(',')])



