declare interface ICredentials {
  email: string;
  password: string;
}

declare interface IUser {
  id: number;
  is_staff: boolean;
  email: string;
  first_name: string;
  last_name: string;
}

declare interface IRegistrationForm {
  email: string;
  first_name: string;
  last_name: string;
  password1: string;
  password2: string;
}

declare interface IUpdateProfileForm {
  email: string;
  first_name: string;
  last_name: string;
  password1?: string;
  password2?: string;
}