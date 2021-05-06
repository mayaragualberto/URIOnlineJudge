
//Recebe o placar dos jogos Inter x Grêmio e informa a quantidade de partidas, 
//quantidade de gols de cada time e o vencedor
import java.util.Scanner;

public class URI1131 {
    public static void main(String[] args) {
        int grenal, partidanova, gols_inter, gols_gremio, vit_inter, vit_gremio, empates;
        partidanova = 1;
        grenal = vit_inter = vit_gremio = empates = 0;
        Scanner input = new Scanner(System.in);
        do {
            gols_inter = input.nextInt();
            gols_gremio = input.nextInt();
            if (gols_inter == gols_gremio) {
                empates++;
            } else if (gols_inter > gols_gremio) {
                vit_inter++;
            } else if (gols_inter < gols_gremio) {
                vit_gremio++;
            }
            System.out.println("Novo grenal (1-sim 2-nao)");
            partidanova = input.nextInt();
            grenal++;
        } while (partidanova != 2);
        System.out.println(grenal + " grenais");
        System.out.println("Inter:" + vit_inter);
        System.out.println("Gremio:" + vit_gremio);
        System.out.println("Empates:" + empates);
        if (vit_inter > vit_gremio) {
            System.out.println("Inter venceu mais");
        } else if (vit_inter < vit_gremio) {
            System.out.println("Gremio venceu mais");
        } else {
            System.out.println("Nao houve vencedor");
        }

    }
}
