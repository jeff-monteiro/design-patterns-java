package br.com.patterns.factory.apple.factory;

import br.com.patterns.factory.apple.model.IPhone;
import br.com.patterns.factory.apple.model.IPhoneXSMax;

public class IPhoneXSMaxFactory extends IPhoneFactory{

    public IPhone createIPhone(){
        return new IPhoneXSMax();
    }
    
}
