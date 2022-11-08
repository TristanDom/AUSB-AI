import ExtractorDeCodigo.Scripper
import ConversorCodigoBinario.Conversor


codWeb = ExtractorDeCodigo.Scripper.extraccionCodigoWeb()

codBin = ConversorCodigoBinario.Conversor.texto_a_binario(codWeb)

print(codBin)

