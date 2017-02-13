 Trabalhos segurança


T1 - Implementação Diffie-Hellman
   Para testar basta inicializar duas instâncias de dh.py passando como parâmetro um valor inteiro que representa a chave privada.
   Após inicializar, é necessário copiar a chave compartilhada para o outro "cliente". Assim, ambas as chaves calculadas deverão ser iguais.
   
   
   ex: python3 dh.py 80:
       	       --chave pública : 12698830608 
       python3 dh.py 15:
       	       --chave pública: 107430705947


       Trocando as chaves entre os dois, temos como resultado: 56838093148.
       
 T2 - Implementação AES256
 	Para testar basta executar o arquivo aes256.py
 	Como resultado, o algoritmo exibe a mensagem original, criptografada e decriptografada.
 	A chave é adaptada para um hash SHA256, e posteriormente executado na função de AES.
 	
 T3 - Implementação RSA
 	Para testar, basta executar o arquivo rsa.py
 	Como resultado, o algoritmo exibe a mensagem criptografada e decriptografada.
 	
 T4 - Certificado digital
      	O arquivo cd.py gera uma string como 'arquivo' concatenado com o hash e a chave pública, cd.py também verifica se há um certificado válido. No início da string, os primeiros 32bytes representam o tamanho do texto, hash e chave pública respectivamente.
 
 T5 - Buffer Overflow
        Execute o arquivo "udpserver",
        Então execute o arquivo "udpclient".
        Ao inicializar o cliente, no servidor será acessado uma função indevida, causada pelo bufferOverflow.
        
T6 - Criptografia clássica
	importas as funções dos algoritmos do arquivo 'cc.py'. Cada Algoritmo clássico, recebe uma chave e um array de bytes (mapeados aos valores de 0 a 255).
	Ceasar:
		encryCeasar(data,k) : recebe um array de bytes (valores de 0 a 255), e uma chave K. Devolve um array de bytes correspondente a criptografia.
		decryCeasar(data,k): Recebe um array de bytes e uma chave k, e devolve um array de bytes com a sequência correspondente.
	Vigenere:
		encryVigenere(data,keys): Array de bytes e uma chave k. Retorna um array de bytes correspondente.
		decryVigenere(data,keys): Array de bytes e uma chave k como entrada. Retorna o array de bytes.
	Transposição:
		encryTransposition(data,k):recebe o array e a chave, e devolve um array conforme o algoritmo.
		decryTransposition(data,k):Recebe o array e a chave, e devolve um array.
	Substituição:
		encrySubs(data,k): Recebe o array de bytes e a chave, e devolve um array com cifra de substituição 
		decrySubs(data,key): Recebe o array de bytes e uma chave para esta cifra, e devolve o vetor de bytes decriptografado.
	As implementações estão no arquivo 'cc.py' dentro da pasta CC.

 T7 - Quebrar cifras em posse do texto original
 	O arquivo de execução dos teste encontra-se em 'main.py' dentro da pastas CC
 	
 T8 - Quebrar cifras com força-bruta
 	A implementação encontra-se no arquivo 'breaker.py' dentro da pasta BruteForce.
 	O arquivo teste é o 'main.py' dentro da mesma pasta.
 	
 T9 - Entropia
 	Dentro da pasta Entropia, basta executar o arquivo 'entropy.py'.
 	O teste em questão é feito apenas sobre o arquivo '7.inputs.sub.X'.
 
 T10 - Padrões
 	Dentro da pasta Padroes, basta executar o arquivo 'pattern.py'.
 	
 	
 
 
 