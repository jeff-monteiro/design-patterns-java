package br.com.patterns.factory.apple.factory;

import br.com.patterns.factory.apple.model.IPhone;
import br.com.patterns.factory.apple.model.IPhoneX;

public class IPhoneXFactory extends IPhoneFactory {

    public IPhone createIPhone(){
        return new IPhoneX();                                                                                                                       
    }
    
}
