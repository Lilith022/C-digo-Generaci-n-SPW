#include <iostream>
#include <fstream>
# include <vector>
#include <cmath>

int main() {
double f = 2400;  // Frequency of the triangular signal
double dt = 1 / (f * 50);  // Time step
int numPoints = 400;  // Number of data points
std::vector<double> t(numPoints);
std::vector<double> sinwave(numPoints);
std::vector<double> triangular_wave(numPoints);
std::vector<int> Vq1(numPoints);
std::vector<int> Vq4(numPoints);
std::vector<int> Vq2(numPoints);
std::vector<int> Vq3(numPoints);

// Generate time vector and triangular and sinusoidal waves
for (int i = 0; i < numPoints; i++) {
    t[i] = i * dt;
    sinwave[i] = sin(377*t[i])*0.98;
    triangular_wave[i] = 5 * (t[i] - floor(t[i] + 0.5));
}

// Generate Q1, Q4, Q2, and Q3 signals
for (int i = 0; i < numPoints; i++) {
    Vq1[i] = (sinwave[i] > triangular_wave[i]) ? 5 : 0;
    Vq4[i] = (sinwave[i] < -triangular_wave[i]) ? 5 : 0;
    Vq2[i] = (-sinwave[i] > triangular_wave[i]) ? 5 : 0;
    Vq3[i] = (-sinwave[i] < -triangular_wave[i]) ? 5 : 0;
}

// Save data to TSV files
std::ofstream file1("5VPQ1.tsv");
std::ofstream file4("5VPQ4.tsv");
std::ofstream file2("5VPQ2.tsv");
std::ofstream file3("5VPQ3.tsv");

for (int i = 0; i < numPoints; i++) {
    file1 << t[i] << "\t" << Vq1[i] << "\n";
    file4 << t[i] << "\t" << Vq4[i] << "\n";
    file2 << t[i] << "\t" << Vq2[i] << "\n";
    file3 << t[i] << "\t" << Vq3[i] << "\n";
}

file1.close();
file4.close();
file2.close();
file3.close();

return 0;
}
}