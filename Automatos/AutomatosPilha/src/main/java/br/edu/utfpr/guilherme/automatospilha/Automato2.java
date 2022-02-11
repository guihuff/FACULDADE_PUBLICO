/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package br.edu.utfpr.guilherme.automatospilha;

import static br.edu.utfpr.guilherme.automatospilha.Principal.Imprimir;
import static br.edu.utfpr.guilherme.automatospilha.Principal.limparPilha;
import java.util.Stack;

/**
 *
 * @author CLIENTE
 */
public class Automato2 {

    public void Testar2(String entrada){
        Stack<Character> pilha = new Stack();
        limparPilha(pilha);
        pilha.push('Z');
        int posicao = 0;
        int estado = 0;
        while(posicao < entrada.length() && !pilha.empty()){
                Imprimir(entrada, estado, posicao);

                char elemento = entrada.charAt(posicao);

                if(estado == 0 && elemento == 'a' && pilha.peek() == 'Z'){
                    estado = 1;
                    pilha.pop();
                    pilha.push('Z');
                    pilha.push('A');
                    pilha.push('A');
                }else{
                    if(estado == 0 && elemento == 'b' && pilha.peek() == 'Z'){
                        estado = 2;
                        pilha.pop();
                        pilha.push('Z');
                    }else{
                        if(estado == 1 && elemento == 'a' && pilha.peek() == 'A'){
                            estado = 1;
                            pilha.pop();
                            pilha.push('A');
                            pilha.push('A');
                            pilha.push('A');
                        }else{
                            if(estado == 1 && elemento == 'b' && pilha.peek() == 'A'){
                            estado = 2;
                            pilha.pop();
                            pilha.push('A');
                            }else{
                                if(estado == 2 && elemento == 'c' && pilha.peek() == 'A'){
                                   estado = 2;
                                   pilha.pop();
                                }else{
                                    if(estado == 2 && elemento == 'd' && pilha.peek() == 'Z'){
                                        estado = 3;
                                        pilha.pop();
                                        pilha.push('Z');
                                    }else{
                                        if(estado == 3 && elemento == 'd' && pilha.peek() == 'Z'){
                                            estado = 3;
                                            pilha.pop();
                                            pilha.push('Z');
                                        }else{
                                            if(estado == 3 && elemento == 'e' && pilha.peek() == 'Z'){
                                                estado = 4;
                                                pilha.pop();
                                                pilha.push('Z');        
                                            }else{
                                                if(estado == 4 && elemento == 'e' && pilha.peek() == 'Z'){
                                                    estado = 5;
                                                    pilha.pop();
                                                    pilha.push('Z');
                                                }else{
                                                    if(estado == 4 && elemento == 'e' && pilha.peek() == 'A'){
                                                        estado = 5;
                                                        pilha.pop();
                                                        pilha.push('A');
                                                    }else{
                                                        if(estado == 5 && elemento == 'e' && pilha.peek() == 'Z'){
                                                            estado = 6;
                                                            pilha.pop();
                                                            pilha.push('Z');
                                                        }else{
                                                            if(estado == 5 && elemento == 'e' && pilha.peek() == 'A'){
                                                                estado = 6;
                                                                pilha.pop();
                                                                pilha.push('A');
                                                            }else{
                                                                if(estado == 6 && elemento == 'e' && pilha.peek() == 'Z'){
                                                                    estado = 4;
                                                                    pilha.pop();
                                                                    pilha.push('Z');
                                                                    pilha.push('A');
                                                                }else{
                                                                    if(estado == 6 && elemento == 'e' && pilha.peek() == 'A'){
                                                                        estado = 4;
                                                                        pilha.pop();
                                                                        pilha.push('A');
                                                                        pilha.push('A');
                                                                    }else{
                                                                        if(estado == 6 && elemento == 'f' && pilha.peek() == 'A'){
                                                                            estado = 7;
                                                                            pilha.pop();
                                                                        }else{
                                                                            if (estado == 6 && elemento == 'f' && pilha.peek() == 'Z'){
                                                                                estado = 8;
                                                                                pilha.pop();
                                                                            }else{
                                                                                if (estado == 7 && elemento == 'f' && pilha.peek() == 'Z'){
                                                                                    estado = 8;
                                                                                    pilha.pop();
                                                                                }else{
                                                                                    if (estado == 7 && elemento == 'f' && pilha.peek() == 'A'){
                                                                                        estado = 7;
                                                                                        pilha.pop();
                                                                                    }else{
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
                                }         
                            }   
                        }      
                    }
                }

                posicao++;
            }
            Imprimir(entrada, estado, posicao);

            
            if(estado == 8){
                System.out.println("(( ACEITA ))");

            }else{
                System.out.println("(( Rejeita ))");
            }
    }

}
