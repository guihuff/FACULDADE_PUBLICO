package br.edu.utfpr.guilherme.automatospilha;


import java.util.Random;
import java.util.Scanner;
import java.util.Stack;



public class Principal {
    
    public static void main(String[] args) {
        Automato2 a = new Automato2();
        
        Scanner s = new Scanner(System.in);
        
        System.out.println("=======================================================\\");
        
        for(int i = 0; i < 10; i++){
            System.out.println("======================================");
            System.out.println("Palavra: " + (i+1));   
            System.out.println("Digite a cadeia");
            String entrada = gerapalavrasCertas();
            automato(entrada);
        }
        System.out.println("===========Incoretas===============");
        automato("bcdefff");
        System.out.println("===========Incoretas===============");
        automato("abccdeef");
        System.out.println("===========Incoretas===============");
        automato("abdeeef");
        System.out.println("===========Incoretas===============");
        automato("accdeeef");
        System.out.println("===========Incoretas===============");
        automato("b");
        
        System.out.println("=======================================================\\");
        System.out.println("Inicio 2");
        System.out.println("=======================================================\\");
        
        for(int i = 0; i < 10; i++){
            System.out.println("======================================");
            System.out.println("Palavra: " + (i+1));   
            System.out.println("Digite a cadeia");
            String entrada2 = gerapalavrasCertas();
            a.Testar2(entrada2);
        }
        System.out.println("===========Incoretas===============");
        a.Testar2("bcdefff");
        System.out.println("===========Incoretas===============");
        a.Testar2("abccdeef");
        System.out.println("===========Incoretas===============");
        a.Testar2("abdeeef");
        System.out.println("===========Incoretas===============");
        a.Testar2("accdeeef");
        System.out.println("===========Incoretas===============");
        a.Testar2("b");
        System.out.println("=======================================================\\");
        
        
        
        
    }
    public static void automato(String entrada){
        Stack<Character> pilha = new Stack();
        limparPilha(pilha);
        pilha.push('Z');
        int posicao = 0;
        int estado = 0;
        while(posicao < entrada.length() && !pilha.empty()){
                Imprimir(entrada, estado, posicao);

                char elemento = entrada.charAt(posicao);

                if(estado == 0 && elemento == 'a' && pilha.peek() == 'Z'){
                    estado = 0;
                    pilha.pop();
                    pilha.push('Z');
                    pilha.push('X');
                    pilha.push('X');
                }else{
                    if(estado == 0 && elemento == 'a' && pilha.peek() == 'X'){
                        estado = 0;
                        pilha.pop();
                        pilha.push('X');
                        pilha.push('X');
                        pilha.push('X');
                    }else{
                        if(estado == 0 && elemento == 'b' && pilha.peek() == 'Z'){
                            estado = 1;
                            pilha.pop();
                            pilha.push('Z');
                        }else{
                            if(estado == 0 && elemento == 'b' && pilha.peek() == 'X'){
                            estado = 1;
                            pilha.pop();
                            pilha.push('X');
                            }else{
                                if(estado == 1 && elemento == 'c' && pilha.peek() == 'X'){
                                   estado = 1;
                                   pilha.pop();
                                }else{
                                    if(estado == 1 && elemento == 'd' && pilha.peek() == 'Z'){
                                        estado = 2;
                                        pilha.pop();
                                        pilha.push('Z');
                                    }else{
                                        if(estado == 2 && elemento == 'd' && pilha.peek() == 'Z'){
                                            estado = 2;
                                            pilha.pop();
                                            pilha.push('Z');
                                        }else{
                                            if(estado == 2 && elemento == 'e' && pilha.peek() == 'Z'){
                                                estado = 3;
                                                pilha.pop();
                                                pilha.push('Z');
                                                pilha.push('X');
                                            }else{
                                                if(estado == 3 && elemento == 'e' && pilha.peek() == 'X'){
                                                    estado = 4;
                                                    pilha.pop();
                                                    pilha.push('X');
                                                }else{
                                                    if(estado == 4 && elemento == 'e' && pilha.peek() == 'X'){
                                                        estado = 5;
                                                        pilha.pop();
                                                        pilha.push('X');
                                                    }else{
                                                        if(estado == 5 && elemento == 'e' && pilha.peek() == 'X'){
                                                            estado = 3;
                                                            pilha.pop();
                                                            pilha.push('X');
                                                            pilha.push('X');
                                                        }else{
                                                            if(estado == 5 && elemento == 'f' && pilha.peek() == 'X'){
                                                                estado = 6;
                                                                pilha.pop();
                                                            }else{
                                                                if(estado == 6 && elemento == 'f' && pilha.peek() == 'X'){
                                                                    estado = 6;
                                                                    pilha.pop();
                                                                }else{
                                                                    pilha.push('S');//Para rejeitar qualquer elemento indesejado
                                                                    //Quando chegava no estado 6 e tinha mais fs que o permitido aceitava
                                                                    break;
                                                                }                          
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }         
                            }   
                        }      
                    }
                }

                posicao++;
            }
            Imprimir(entrada, estado, posicao);

            if(estado == 6 && pilha.peek() == 'Z'){
                estado = 7;
                pilha.pop();
                Imprimir(entrada, estado, posicao);
            }
            if(estado == 7){
                System.out.println("(( ACEITA ))");

            }else{
                System.out.println("(( Rejeita ))");
            }
    }
    
    public static void Imprimir(String entrada, int estado, int po){
        System.out.print(entrada.substring(0, po));
        System.out.print("[q"+estado+"]");
        System.out.println(entrada.substring(po));
    }
    
    public static void limparPilha(Stack pilha){
        while(!pilha.isEmpty()){
            System.out.println(pilha.pop());
        } 
    }
    public static String gerapalavrasCertas(){
        int m, n, x;
        Random random = new Random();
        String palavra = "b";
        n = random.nextInt(10);
        x = random.nextInt(5);
        m = random.nextInt(5);
        x++;
        m++;
        for (int i = 0; i < n; i++) {
            palavra = 'a' + palavra ;
        }

        for (int i = 0; i < n*2; i++) {
            palavra = palavra + 'c';
        }
        for (int i = 0; i < x; i++) {
            palavra = palavra + 'd';
        }
        for (int i = 0; i < 3*x; i++) {
            palavra = palavra + 'e';
        }
        for (int i = 0; i < x; i++) {
            palavra = palavra + 'f';
        }
        
        return palavra;
    }
    
}
