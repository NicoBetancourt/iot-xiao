from transformers import pipeline

def initialize_generator():
    """
    Inicializa el generador de máscaras utilizando la biblioteca Transformers.
    
    Returns:
        pipeline: Objeto pipeline para la generación de máscaras.
    """
    # Inicializa el pipeline para la generación de máscaras
    generator = pipeline(
        task="mask-generation",  # Especifica la tarea como generación de máscaras
        model="nielsr/slimsam-77-uniform",  # Especifica el modelo pre-entrenado a utilizar
        # device=0,  # Especifica el dispositivo de procesamiento (GPU si está disponible)
        points_per_batch=256  # Especifica el número de puntos por lote
    )
    
    return generator
