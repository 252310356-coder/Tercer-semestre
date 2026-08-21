#include <iostream>
#include <windows.h>

using namespace std;

int main()
{
    // 1 millón de caracteres = 1 MB exacto por iteración
    const int TAM = 1000000; 
    int segundos = 0;
    int iteraciones = 0;
    double totalMB = 0;

    cout << "--- INICIANDO PRUEBA CON CHAR (ACUMULATIVA) ---" << endl;

    while (true)
    {
        int* datos = new int[TAM];

        // Forzamos la escritura en la memoria (4 bytes por cada int)
        for (int i = 0; i < TAM; i++) {
            datos[i] = i;
        }

        totalMB += (double)(TAM * sizeof(int)) / (1024.0 * 1024.0);
        cout << "Memoria acumulada aprox: " << totalMB << " MB\n" << flush;

        iteraciones++;
        // Como cada vuelta tiene Sleep(500), cada 2 iteraciones pasa 1 segundo aprox.
        if (iteraciones % 2 == 0) {
            segundos++;
            if (segundos % 5 == 0) {
                cout << "===> Segundos transcurridos: " << segundos << " <===\n" << flush;
            }
        }

        Sleep(500);
    }

    return 0;
}