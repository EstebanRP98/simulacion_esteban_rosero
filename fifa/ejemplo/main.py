import papermill as pm
import argparse 

def main(numeros):
    pm.execute_notebook('Untitled.ipynb',
                    'output.ipynb',
                    parameters=dict(a=numeros[0],b=numeros[1])
    )

if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument(
        'int',
        help='pasar A y B',
        type=str
    )

    arguments = args.parse_args()

    main([i for i in arguments.int.split(',')])